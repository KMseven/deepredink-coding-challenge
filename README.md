# deepredink-coding-challenge
The python code takes voice input from the user and pass the input to the [Poki API](https://pokeapi.co/ "POKEAPI") and reads the link of the image and displays it in the browser

### Prerequisites

* [PyAudio](https://pypi.python.org/pypi/PyAudio "python library")
* [Speech Recognition](https://pypi.python.org/pypi/SpeechRecognition/ "python library")
* [requests](http://docs.python-requests.org/en/master/ "python library")
* [webbrowser](https://docs.python.org/2/library/webbrowser.html "python library")
* [requests_cache](https://pypi.python.org/pypi/requests-cache "python library")
* [Fake-useragent](https://pypi.python.org/pypi/fake-useragent "python library")

### Things to look at
* There is possibility of getting print lag when run in spyder.
* While running the unitest code you may get the **certificate not found** error.Search for cacert.pem certificate in anaconda site-packages(C:\Users\username\Anaconda\Lib\site-packages) and paste it in certifi(C:\Users\username\Anaconda\Lib\site-packages\certifi)
    
### Notes

Apart from main there are two other functions in the code
* listen    :Takes the voice input and return text
* response  :Sends the input to the Poki API, reads the response and displays the image in the browser 

I used google speech recognition API for getting voice input, would have used sphinx if the program should run offline

I used fake_useragent library for getting the chrome useragent.(Without using this you can even directly copy paste chrome's useragent)

I used request_cache to cache the all the responses with status code 200.

I did unit testing to the code, It passed all the test cases given by me.For you to test I had written the test_complete function
