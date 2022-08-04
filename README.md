# combine-like-audio
A Python script to combine like audio files based on a key:value CSV file.


This script was designed to take in a set of audio files, look them up in a CSV, and output a set of combined audio files based on their characteristics. It was intended for linguistics research.

For example, imagine you have a set of audio files labeled 001.wav, 002.wav, 003.wav and so on. Each file is a recording of one word. You can use this script to combine them by any feature that you specify. I have included sample files in the Example folder to illustrate this introduction.

Imagine that you have created a CSV that looks like this, without the headers. You, the researcher, know that file 1 is a recording of "cat," file 2 is a recording of "tap," and so on down the list. 

| File number | Name (ignored by script) 
|--|--|
| 001 | cat |
| 002 | tap |
| 003 | hat |
| 004 | lap |
| 005 | sat |
| 006 | nap |

Suppose that you want to label the files by their rhyme. In a new column, add the rhyme for each word.

| File number | Name (ignored by script) | Category |
|--|--|--|
| 001 | cat | at |
| 002 | tap | ap |
| 003 | hat | at |
| 004 | lap | ap |
| 005 | sat | at |
| 006 | nap | ap |

Save this CSV file as "key.csv".

Place the "combine-like-audio.py" script in the same folder as your WAV files and your CSV file, then run the Python script.

Two new WAV files will appear in the folder. One will be all of the "-at" words and the other will be all of the "-ap" words, with a 1/10 second gap separating them.

You can run this script as many times as you like with different categories in the CSV file. The script as is will only work without headers.

| File number | Name (ignored by script) | Category |
|--|--|--|
| 001 | cat | velar |
| 002 | tap | alveolar |
| 003 | hat | glottal |
| 004 | lap | alveolar |
| 005 | sat | alveolar |
| 006 | nap | alveolar |

In this example, the Category field now has three categories referring to the place of articulation of the first consonant. Three new files will appear, with "velar" and "glottal" having just one recording each, and "alveolar" having four.
