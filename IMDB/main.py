import os
from platform import java_ver
# import shutil
import tensorflow as tf
import re
import string
from tensorflow.keras import layers
from tensorflow import keras


train_data = os.listdir("aclImdb/train")
train_dir = "aclImdb/train"
raw_train_df = tf.keras.utils.text_dataset_from_directory(train_dir
    ,batch_size=32, 
    validation_split=0.2, 
    subset='training', 
    seed=42)

raw_val_ds = tf.keras.utils.text_dataset_from_directory(
    'aclImdb/train', 
    batch_size=32, 
    validation_split=0.2, 
    subset='validation', 
    seed=42)

raw_test_ds = tf.keras.utils.text_dataset_from_directory('aclImdb/test', batch_size=32)


sample = '''It\'s difficult to know where this adaptation starts going wrong, because I think the problem begins with the books themselves. Alexander McCall Smith has worked out that you read them not for the detective stories, but for his deeply condescending and completely spurious vision of an Africa that does not exist. He\'s done for Botswana what Borat did for Kazakhstan - not as successfully, but based in as much fact.<br /><br />Once I realised this, it ceased to gall me that Jill Scott, an American singer/actress, is cast as Mma Ramotswe. If she is to represent a land that is not Africa, how appropriate that she is a black woman who is not African? She\'s not the only American on the cast; Mma Makutsi is played by Anika Noni Rose. Both women are far, far too young for the roles they\'re playing, and far too glamorous. Both brutally murder the local accents, and both focus so entirely on this brutality that they fail to offer much in the way of acting. Scott\'s Mma Ramotswe is bouncy, cute and soft. Rose\'s Mma Makutsi is an annoying motor-mouthed bitch.<br /><br />The result is almost unwatchable. The principal cast is redeemed only by the presence of Lucian Msamati, who turns in a decent performance as Mr JLB Matekoni. Hes comes off smarter and more intense than in the books, but I find myself unable to blame Msamati for this - he\'s a shining light in an ocean of suckage. The contradictions between his performance and the books are clearly laid at the feet of whichever committee of butchers wrote the script.<br /><br />To me, McCall Smith\'s writing has always been highly entertaining yet notoriously bad. He refuses to be edited. As a result, his books contain experiments in grammar that border on the scientific, and characters that change name mid-sentence. It is therefore something of an achievement that the writing team on this project actually made it worse.<br /><br />The dialogue is now largely Anglicised. Characters speak of "opening up" and "sensitivity to needs". Mma Ramotswe and Mr JLB Matekoni flirt openly. Mma Makutsi moans about not having a computer, but given her constantly restyled hair, makeup and jewellery, I\'m surprised she doesn\'t have a MacBook in her handbag along with her Visa card.<br /><br />So what are we left with here? It\'s difficult to be upset with this crappy adaptation because honestly, most of the things I like about the original books are apocryphal anyway. McCall Smith paints a fictional Botswana populated with cute, non-threatening black people who are full of amusing and palatable wisdom-nuggets. It reads well despite linguistic travesty, but it is a vision of how a certain type of white person wishes black people were. It just isn\'t true.<br /><br />Given that, it\'s hardly surprising that this show sucks as much as it does. It remains to be seen whether European and American audiences will even notice, however.'''

def custom_standardization(input_data):
  lowercase = tf.strings.lower(input_data)
  stripped_html = tf.strings.regex_replace(lowercase, '<br />', ' ')
  return tf.strings.regex_replace(stripped_html,
                                  '[%s]' % re.escape(string.punctuation),
                                  '')

maximum_features = 100000
sequence_length = 250

vectorize_layer = layers.TextVectorization(
    standardize=custom_standardization,
    max_tokens=maximum_features,
    output_mode='int',
    output_sequence_length=sequence_length)


train_text = raw_train_df.map(lambda x, y: x)
vectorize_layer.adapt(train_text)

def vectorize_text(text, label):
  text = tf.expand_dims(text, -1)
  return vectorize_layer(text), label

from keras import losses

model = keras.models.Sequential([
  layers.Embedding(maximum_features+1,16),
  layers.Dropout(0.2),
  layers.GlobalAveragePooling1D(),
  layers.Dropout(0.2),
  layers.Dense(1)])
  
model.compile(loss=losses.BinaryCrossentropy(from_logits=True),optimizer='adam',metrics=tf.metrics.BinaryAccuracy(threshold=0.0))

train_ds = raw_train_df.map(vectorize_text)
val_ds = raw_val_ds.map(vectorize_text)
test_ds = raw_test_ds.map(vectorize_text)

epochs = 10
history = model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=epochs)

loss, accuracy = model.evaluate(test_ds)



export_model = tf.keras.Sequential([
  vectorize_layer,
  model,
  layers.Activation('sigmoid')
])

export_model.compile(
    loss=losses.BinaryCrossentropy(from_logits=False), optimizer="adam", metrics=['accuracy']
)

# Test it with `raw_test_ds`, which yields raw strings
loss, accuracy = export_model.evaluate(raw_test_ds)
print(accuracy)

examples = [
  "how ambitious people get their destiny"
]

predicted = export_model.predict(examples)
print(predicted)