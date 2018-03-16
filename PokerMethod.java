import java.util.Scanner;

/* -Cory Cothrum
 * -2/20/18
 * This is a software implementation of the Poker Cipher - a personally developed Cipher utilizing only a deck of cards and pen+paper.
 * A software implementation is faster and educational, but ultimately less secure then the standard physical process 
 * (plaintext can be retrieved from memory etc.)
 * 
 * -2/26/18
 * 
 */

public class pokerCipher {

	public static void main(String[] args) {
		/* -POKER CIPHER-
		 * Take message, phrase, and deck of cards to produce and encrypted message decryptable only with an identical deck.
		 * Input from file or keyboard, Output to file or screen
		 * 
		 * +=ENCRYPTION=+
		 * 
		 * 1. Input or Create shuffled 'deck' of cards
		 * 
		 * 2. Split into 2 sets of red and black
		 * 	2a. Encode to separate alphabets
		 * 
		 * 3. Take message
		 * 	3a. Strip message down into alphabet only
		 * 	3b. Encode message into cards (alternating letters between red/black sets)
		 * 	3c. Recombine message
		 * 
		 * 4. Get secret phrase
		 * 	4a. Pad new message to phrase length
		 * 	4b. Resort secret phrase in order
		 *  4c. sort message according to offsets
		 * 
		 * 5. Encode using 'Quifid' boxes
		 * 	5a. Pad suits with garbage values
		 * 
		 * 6. Output encrypted message
		 * 
		 * 
		 * -=DECRYPTION=-
		 * 
		 * 1. Input Ciphertext
		 *  1a. Remove values
		 *  1b. Grab letter from Quifid box
		 *  1c. Return card from red/black grid
		 *  1d. Reform message by card values
		 *  
		 * 2. Sort phrase, get sort values
		 *  2a. 'Unsort' message according to offset values
		 * 
		 * 3. Pull letter from alphabet grid (red/black alternating)
		 * 
		 * 4. Reform message, output
		 */
		
		Scanner keyboard = new Scanner(System.in);
		
		/* -DECK MAKER -
		 * Create a deck of 52 cards of 4 suits and 13 values, shuffle deck, output complete array
		 */ 
		
		String[] deck = new String[52], 
				suits = new String[]{"H","S","D","C"}, 
				values = new String[]{"A", "2", "3", "4", "5", "6", "7", "8", "9", "0", "J", "Q", "K"};
		
		int x, y, z = 0;
		for (y = 0; y < suits.length; y++) //insert values/suits length properly
		{
			for (x = 0; x < values.length ; x++)
			{
			deck[z++] = values[x] + suits[y];
			}
		}
		
		/* -SHUFFLER-
		 * Shuffles cards 10x
		 * 
		 * -grabs first and last cards, places first card anywhere, even behind last, and continues until it finds the 'first' last card.
		 * -ideally takes a number of shuffles
		 */
		
		int shuffles;
		String lastCard, currentCard;
		
		shuffles = 10;
		
		for (int i = 0; i < shuffles; i++)
		{
			lastCard = deck[51];
			currentCard = deck[0];
			while (currentCard != lastCard)
			{
				//insert current into deck, anywhere [reform array - shuffled deck array?]
				//grab new current card
				//repeat
				
			}
		}
		
		//Separate red/black cards - assign to letters for encoding - 2D array of letter and value
		//preserve relative order
		
		//DECK IS NEEDED TO DECODE MESSAGE - EITHER HAVE A DUPLICATE, OR TRANSMIT THIS (NOT RECOMENDED)
		
		/* -MESSAGE INPUT-
		 * -in cryptography-
		 * Raw, unprocessed text is called PLAINTEXT, 
		 * The Encrypted message is called CIPHERTEXT, 
		 * A Decrypted message is called CLEARTEXT (NOT PLAINTEXT)
		 */
		
		String messagePlaintext, messageCiphertext;
		
		System.out.println("Please enter message to be encoded:\n");
		messagePlaintext = keyboard.nextLine();
		
		//split into red and black sets
		for (int curCard = 0; curCard < messagePlaintext.length(); curCard++)
		{ //run through the current card, do odd even test to separate to sets
			if (curCard%2 != 0)
			{
				//add card value associated with letter from black alphabet from messagePlaintext[curCard] to messageCiphertextOne
			}
			else
			{
				//add card value associated with letter from from messagePlaintext[curCard] red alphabet to messageCiphertextOne
			}
		}
		
		//encode message into card values according to red/black alphabets and red/black sets of message
		
		
		
		
		
		/* -PHRASE INPUT-
		 * -input key phrase, then create a second sorted copy for later 
		 * -or-
		 * HARD
		 * -dont split phrase up; grab first value, see how it stacks up among the rest (evens)- 
		 * -grab lowest character, make new #1; grab next, see how it stacks up to (odds), make #2
		 * repeat
		 */
		
		String keyPhrase, sortedKeyPhrase, lowestChar, currentChar;
		
		System.out.println("Please enter the key phrase:\n");
		keyPhrase = keyboard.nextLine();
		if (keyPhrase.length()%2 != 0)
			keyPhrase += "x"; //pad to ensure proper handling of suits + values
		
		for (int curChar = 0; curChar < keyPhrase.length() ; curChar++)
		{
			//if its not a $
			//lowestChar = keyPhrase[curChar];
			//while loop - while (you havent hit the character you started with)
			//go through every other letter and check for alphebetization. 
			//new lowest = keyPhrase[position]
			//replace with $ as sentinel
		}
		
		
		
		
		/* -MESSAGE PADDING-
		 * pad message by message.length() % keyPhrase.length() to ensure proper shifting later on
		 */
		
		int suitI = 0; //suit Index, for 'randomly' adding aces - implement actual random aces/cards
		while (messagePlaintext.length()%keyPhrase.length() > 0)
		{
			//append Ace's to messagePlaintext
			messagePlaintext += ("A" + (suits[(suitI++)%4]));
		}
		
		
		/* -MESSAGE SORT-
		 * -sort message according to the phrase
		 * -REQUIRES sort offsets from the key phrase (relative to phrase not alphabet)
		 * break message into phrase blocks, assign to 2D array assigned with phrase letter and sort by them based on phrase offsets
		 * -loop through array of offsets, grab from selected block into the new message
		 * 
		 * -also-
		 * must consider row shifting...
		 * 
		 * SORTING IN GROUPS
		 * EG: "messageisherexxxxx" -english message used for clarity - normally would be cards
		 * 
		 * 1|2|3|4|5|6
		 * A;B;A;B;A;B - group
		 * S|E|C|R|E|T - unsorted phrase
		 * ===========
		 * m|e|s|s|a|g
		 * e|i|s|h|e|r
		 * e|x|x|x|x|x
		 * 
		 * SECRET - SCE + ERT
		 * SCE -> CES
		 * ERT -> ERT
		 * SECRET - CEERST
		 * 
		 * 3|2|5|4|1|6 - sort offsets
		 * A;B;A;B;A;B
		 * C|E|E|R|S|T
		 * ===========
		 * s|e|a|s|m|g
		 * s|i|e|h|e|r
		 * x|x|x|x|e|x
		 * 
		 * -> "seasmgsieherxxxxex"
		 * 
		 * ROW SORTING
		 *   3|2|5|4|1|6
		 *   A;B;A;B;A;B
		 *   C|E|E|R|S|T
		 * =============
		 * S]s|e|a|s|m|g[1
		 * E]s|i|e|h|e|r[2
		 * C]x|x|x|x|e|x[3
		 * R]
		 * E]
		 * T]
		 * 
		 * SECRET -> SEC (truncate - do not sort unassigned letters)
		 * SEC -> CES
		 * 
		 *   3|2|5|4|1|6
		 *   A;B;A;B;A;B
		 *   C|E|E|R|S|T
		 * =============
		 * C]x|x|x|x|e|x[3
		 * E]s|i|e|h|e|r[2
		 * S]s|e|a|s|m|g[1
		 * 
		 * -> "xxxxexsieherseasmg"
		 */
		
		//sort here
		
		
		/* -QUIFID ENCODING-
		 * A deck of cards encompasses 52 values, or, 4 groups of 13. By treating this as a grid of 4x4 (suits), 
		 * and taking the currently scrambled character from the message, getting its new letter, the letter
		 * can be encoded as a triplet of suits (which box, which row, which column)
		 * EG-
		 * Normal grid for letter substitution
		 * -notice: Red suits comprise top alphabet, Black suits comprise bottom
		 * 
		 * *||A|2|3|4|5|6|7|8|9|0|J|Q|K|
		 * =============================
		 * H||H|r|o|c|x|b|d|n|F|z|q|u|k|
		 * D||p|V|w|y|m|E|s|i|g|j|t|l|a|
		 * C||g|f|Q|v|h|w|Q|l|e|p|D|j|k|
		 * S||u|m|c|y|b|o|x|T|z|i|n|S|r|
		 * 
		 * -notice: Capitalized letters within grid are to be SUBSTITUTED (See *'s)
		 * 
		 * Substituted Quifid boxes
		 * 
		 * _|H|___________|C|___________|D|___________|S|
		 * *|H|C|D|S|:|*|H|C|D|S|:|*|H|C|D|S|:|*|H|C|D|S|
		 * =========|=|=========|=|=========|=|==========
		 * H|*|r|o|c|:|H|x|b|d|n|:|H|*|z|q|u|:|H|*|H|V|Q|
		 * C|p|*|w|y|:|C|m|*|s|i|:|C|g|j|t|l|:|C|a|*|E|A|
		 * D|g|f|*|v|:|D|h|w|*|l|:|D|e|p|*|j|:|D|k|T|F|D|
		 * S|u|m|c|y|:|S|b|o|x|*|:|S|z|i|n|*|:|S|r|S|K|*|
		 * 
		 * -notice: Capitalized letters within boxes are SUBSTITUTED from above values.
		 */
		
		
		
		
		
		
		
		/* -GARBAGE FILL-
		 * -fills newly created suits with randomly selected values added to them. (Just adding values to every other position)
		 */
		
		
		/* -MESSAGE OUTPUT-
		 * -Message is either printed or written to a file.
		 */
		
		//file output handling - message only, with separate file for deck. 
		
		
		
		
		//close open assets
		keyboard.close();
	}
	
	public static void method() {
		
		
		
	}
}







