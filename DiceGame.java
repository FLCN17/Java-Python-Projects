import java.util.Scanner;

/** DiceGame -
 * @author cory cothrum
 * 
 * takes a number of dice, number of sides, and provides 
 * a black-jack style game of trying to hit at or below the mark.
 * 
 * gameLimit is a function of the # dice and sides; approx. two perfect rolls - half of one die
 *
 */
public class DiceGame {
	/**DicePlay -
	 * runs game until someone busts or wins
	 */
	public void DicePlay() {
		String name = "Cory", winner = "None";
		boolean stillRolling = true, holding = false;
		int gameLimit, numDice, sides, rollDice;
		Scanner keyboard = new Scanner(System.in);
		
		System.out.println("Please enter your name: ");
		name = keyboard.nextLine();
		Player player = new Player(name), computer = new Player("CPU");


		//get game settings first time
		System.out.println("Please enter the number of dice: ");
		numDice = keyboard.nextInt(); keyboard.nextLine();
		System.out.println("Please enter the number of sides on the dice: ");
		sides = keyboard.nextInt(); keyboard.nextLine();

		gameLimit = 2 * (numDice * sides) - (sides / 2);
		
		System.out.printf("The bust value is %d\n", gameLimit);
		player.setDice(numDice, sides); computer.setDice(numDice, sides); //set player dice
		do {
			if(!holding) {
				System.out.println("How many dice would you like to roll (-1 to hold)?");
				rollDice = keyboard.nextInt(); keyboard.nextLine();
				if(rollDice == -1)
					holding = true;
				player.roll(rollDice); 
				player.showTotal();
			}
			computer.roll(numDice, gameLimit);
			//System.out.printf("CPU Total: %d\n", computer.getTotal());
			if((computer.getTotal() == gameLimit || player.getTotal() == gameLimit) || (player.getDoneRolling() && computer.getDoneRolling()) || (player.getBust(gameLimit) || computer.getBust(gameLimit))) {
				stillRolling = false;
				winner = (!computer.getBust(gameLimit) && (computer.getTotal() > player.getTotal()%(gameLimit+1)) ? computer.getName() : (!player.getBust(gameLimit) && (player.getTotal() > computer.getTotal()%(gameLimit+1)) ? player.getName() : "None"));
				if(computer.getTotal() == player.getTotal());
			}
		} while(stillRolling);
		computer.showTotal();
		System.out.printf("%s wins!", winner);
		keyboard.close();
	}
	
	/**AdvDicePlay -
	 * Allows for the user to choose a smaller die size to roll with. Only one die at a time. 
	 */
	public void AdvDicePlay() {
		String name = "Cory", winner = "None";
		boolean stillRolling = true, holding = false;
		int gameLimit, numDice, sides, rollDice;
		Scanner keyboard = new Scanner(System.in);
		
		System.out.println("Please enter your name: ");
		name = keyboard.nextLine();
		Player player = new Player(name), computer = new Player("CPU");

		numDice = 1;
		sides = 20;

		gameLimit = 64;
		
		System.out.printf("The bust value is %d\n", gameLimit);
		player.setDice(numDice, sides); computer.setDice(numDice, sides); //set player dice
		do {
			if(!holding) {
				System.out.println("How many dice would you like to roll (-1 to hold)?");
				rollDice = keyboard.nextInt(); keyboard.nextLine();
				if(rollDice == -1)
					holding = true;
				player.roll(rollDice); 
				player.showTotal();
			}
			computer.roll(numDice, gameLimit);
			//System.out.printf("CPU Total: %d\n", computer.getTotal());
			if((computer.getTotal() == gameLimit || player.getTotal() == gameLimit) || (player.getDoneRolling() && computer.getDoneRolling()) || (player.getBust(gameLimit) || computer.getBust(gameLimit))) {
				stillRolling = false;
				winner = (!computer.getBust(gameLimit) && (computer.getTotal() > player.getTotal()%(gameLimit+1)) ? computer.getName() : (!player.getBust(gameLimit) && (player.getTotal() > computer.getTotal()%(gameLimit+1)) ? player.getName() : "None"));
				if(computer.getTotal() == player.getTotal());
			}
		} while(stillRolling);
		computer.showTotal();
		System.out.printf("%s wins!", winner);
		keyboard.close();
	}
}
