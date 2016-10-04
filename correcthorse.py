import random

filename = "20k.txt"

def main(filename):
	words_file = open(filename, 'r')

	words = words_file.read().split("\n")
	temp_words = []
	for word in words:
		temp_words.append(word.strip("\r"))
	words = temp_words

	while True:
		length = int(raw_input("Words:"))
		for i in range(0,length):
			print(words[random.randrange(0,len(words)+1)]),
		print("\n")


if __name__ == "__main__":
	main(filename)