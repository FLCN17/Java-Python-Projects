import java.util.Random;

/** AllWorkAndNoPlayMakesJackADullBoy -
 * @author flcn
 * 
 * outputs the pages from Jacks story in The Shining, with proper typos and formatting.
 * Warning: The entire program /is/ a memory leak
 */
public class AllWorkNoPlayMakesJackADullBoy {

	static Random rand = new Random();
	static int storyLength; //static so the triangle output can mess wit it. real bad i know...
	
	/** Jack -
	 * Sends his story to the typewriter for as long as he is within the overlook hotel.
	 */
	public static void jack() {
		boolean atOverlook = true;
		String story = "All work and no play makes jack a dull boy"; //do you like my story, Wendy?
		while(atOverlook) {
			typeWriter(story);
		}
	}
	
	/** Typewriter -
	 * 
	 * Takes story, decides the amount of pages and lines to use for an output mode, as well as indent and spacing
	 * Also handles resetting the storylength for the triangle output mode
	 * 
	 * @param story - original story
	 */
	public static void typeWriter(String story) {
		//grab pages, decide spacing and mode per output cycle, determine cycles, and determine errors per cycle, repeat
		int pages, indent = 0, mode, lines = 0, spacing = rand.nextInt(3);
		pages = rand.nextInt(20); //how many 'pages' of whatever mode selected to type out
		//get mode
		storyLength = story.length();
		mode = rand.nextInt(4); //randomly choose next 'mode'
		switch(mode) {
		case 0:				//lined output
			indent = rand.nextInt(7);
			lines = rand.nextInt(80);
			break;
		case 1:				//paragraph
			indent = 0;
			lines = rand.nextInt(40);
			break;
		case 2:				//poetry
			indent = rand.nextInt(7) + 5;
			lines = rand.nextInt(10);
			break;
		case 3:				//triangle
			indent = rand.nextInt(4) + 8;
			spacing = 0;
			pages = rand.nextInt(5);
			lines = rand.nextInt(20);
			break;
		}
		for(int x = pages; x-- > 0;) {
			for(int l = lines + 40; l-- > 0;) {
				System.out.print(overlookHotel(story, mode, (mode == 3 ? indent++ : indent), spacing));
				if(storyLength == 0) { //for triangle output, to 'reset' in between calls
					storyLength = story.length();
					System.out.println("");
					indent = rand.nextInt(4) + 8;
				}
			}
		}
	}
	
	/** OverlookHotel -
	 * 
	 * takes a story, and begins passing it to the 'output', adding typos and other maddness using a convoluted system of rands.
	 * 
	 * @param story - original story
	 * @param mode - output format
	 * @param indent - indent before line
	 * @param spacing - line spacing
	 * @return String fixedStory - altered story
	 */
	public static String overlookHotel(String story, int mode, int indent, int spacing) {
		String alphabet = "abcdefghijklmnopqrstuvwxyz,.;:()'?!$%&*#", storyFixed = "";
		int typoRate, caseRate;
		for(int i = (mode == 0 ? (rand.nextInt(7) == 0 ? indent + rand.nextInt(5) : indent ) : indent); i-- > 0;)
			storyFixed += " "; //add indent
		for(int curChar = 0; curChar < storyLength; curChar++) {
			typoRate = rand.nextInt(1000);
			caseRate = rand.nextInt(200)+1;
			if(mode == 2 && rand.nextInt(100) == 0) { //poetry output - randomly make new lines
				storyFixed += "\n";
				for(int r = indent + rand.nextInt(8); r-- > 0;)
					storyFixed += " "; //add random indent to poetry
			}
			if(typoRate >= 5) //5/typoRate chance of typos -within the remaining, however, theres a 1/caserate chance of caps		
				storyFixed += (rand.nextInt(caseRate) == 0 ? story.toUpperCase().charAt(curChar): story.charAt(curChar));
			else if (typoRate >= 2) { // 2/typorate chance of random space added/instead
				storyFixed += " ";
				curChar-= (rand.nextInt(3)==0 ? 0 : 1);
			}
			else //1/typorate chance of real typo
				storyFixed += (rand.nextInt(caseRate) == 0 ? alphabet.toUpperCase().charAt(rand.nextInt(alphabet.length())): alphabet.charAt(rand.nextInt(alphabet.length())));
		}
		if(mode == 0 || mode == 2 || mode == 3)
			storyFixed += "\n";
		else {
			storyFixed += (rand.nextInt(25) == 0 ? "? " : ( rand.nextInt(25) == 0 ? "! " : ". ")); //end of paragraph punctuation
			if(rand.nextInt(5) == 0) {
				storyFixed += "\n";
				if(rand.nextInt(2) == 0)
					storyFixed += "\n";
				for(int r = rand.nextInt(6)+1; r-- > 0;)
					storyFixed += " ";
			}
		}
		if(mode == 3)
			storyLength--;
		for(int s = spacing; s-- > 0;)
			System.out.println("");
		return storyFixed;
	}
	
	public static void main(String[] args) {
		jack();
	}
}
