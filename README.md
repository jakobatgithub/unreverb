# unreverb
Remove reverb from sound

The project aims at removing reverb from sound by using machine learning. Two different use cases come to mind:
1) Remove reverb from music or videos produced e.g. at home by youtubers.
2) Remove reverb from speech transferred by apps as e.g. zoom or whatsapp.
Sound data with reverb can easily be generated from anechoic sound recordings of music and speech for which datasets are available online. Reverb is added by convolution of impulse response functions with the anechoic sound data.
Use case 1) generally requires higher quality of reverb removal than use case 2). The application should run in real time, although for use case 1) it might be sufficient to remove reverb in post production.

useful links:

https://towardsdatascience.com/building-a-reverb-detection-system-using-machine-learning-cba02a1710bf

https://www.openair.hosted.york.ac.uk/

https://pytorch.org/tutorials/beginner/audio_preprocessing_tutorial.html

https://www.gearnews.com/accentize-deroom-remove-reverb/#:~:text=Accentize%20DeRoom%20uses%20AI%20to%20remove%20reverb%20from%20your%20recordings,-11%20Mar%202020&text=Accentize%20has%20released%20DeRoom.,post%20production%20and%20podcasting%20applications

https://librosa.org/doc/main/generated/librosa.feature.inverse.mel_to_audio.html

https://towardsdatascience.com/neural-networks-for-real-time-audio-wavenet-2b5cdf791c4f

https://speechbox.linguistics.northwestern.edu/#!/home

https://www.primacoustic.com/broadway-panels/science/common-reverberation-times/