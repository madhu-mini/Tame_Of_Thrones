# Tame_Of_Thrones
There is no ruler in the universe of Southeros and pandemonium reigns. Shan, the gorilla king of the Space kingdom wants to rule all Six Kingdoms in the universe of Southeros. He needs the support of 3 more kingdoms to be the ruler.
Each kingdom has an animal emblem and Shan needs to send a message with the animal in the message to win them over.
SPACE emblem - Gorilla, LAND emblem - Panda, WATER emblem - Octopus,
ICE emblem - Mammoth, AIR emblem - Owl,
FIRE emblem - Dragon.
    Your coding challenge is to have King Shan send secret message to each kingdom and win them over.Once he wins 3 more kingdoms, he is the ruler! The secret message needs to contain the letters of the animal in their emblem.
For example, secret message to the Land kingdom (emblem: Panda) needs to have the letter 'p','n','d' at-least once and 'a' at-least twice. If he sends "ahdvvnxxxautup" to the Land kingdom, he will win them over.King Shan wants to make sure his secret message is not found by his enemies easily. So he decides to use the oldest of the ciphers 'Seasar cipher’. A cipher is a type of secret code, where you swap the letters around so that no-one can read your
message.To make the secret message encrypted, King Shan uses a secret key, which is the number of characters in the emblem.If King Shan wants to send a message to kingdom Air, he uses the number 3 as the cipher key, as emblem ‘owl’ has 3
characters. So, to encrypt the letter ‘a’, just move 3 letters clockwise on the message wheel, which will give the letter ‘d’.
So if King Shan, sends the message "rozo" to Air, King Shan will receive
the allegiance from Air. As "rozo" will decrypt to "olwl" and these letters
contain the emblem characters ‘o’, ’w’, ’l’.
If King Shan wants to send a message to kingdom Land, he uses the
number 5 as the cipher key, as emblem ‘panda’ has 5 characters. To
encrypt the letter ‘a’, just move 5 letters clockwise on the message
wheel, which will give you the letter ‘f’.<br/>
<br/>
Your program should take the location to the test file as parameter. Input needs to be read from a text file,
and output should be printed to the console.

### Solution with build file
```python
pip install -r requirements.txt
python -m geektrust <absolute_path_to_input_file>
```
### Input
  Input files are available in the input folder.<br/>
  
  For more information visit [A Golden Crown](https://www.geektrust.in/coding-problem/backend/tame-of-thrones).
