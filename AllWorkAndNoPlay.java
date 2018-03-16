
public class allWorkNoPlay {

	public static void jack() {
		int atOverlook = 1, spacing = 1, mode = 0;
		String story = "All work and no play makes jack a dull boy";
		while(atOverlook == 1)
			typeWriter(story);
	}
	
	public static String typeWriter(String story) {
		/*
		 *  if lines:
        message = "     " + message + "     " # replace with a spacing padder; decides indent and fills to next line?
        print(allWorkNoPlayLines(message))
        for i in range(spacing):
            print("")        
    else:
        print(allWorkNoPlayParagraphs(message))
        for i in range(spacing):
            print("")
		 */
		if(lines == )
		return story;
	}
	
	public static void main(String[] args) {
		jack();
		/*

def allWorkNoPlayLines(message):
    #generates lines of typo'd text from an alphabet pool
    capitalError = 10
    firstTypo = 5
    secondTypo = 10
    thirdTypo = 15
    skippedLine = 50
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz     .,:';?/=+1234567890" + '"'
    #message = (' '*rn.randint(0, 3))*rn.randint(0, 4) + message
    if (not rn.randint(0, firstTypo)):
        if (not rn.randint(0, skippedLine)):
            message = ""
        else:
            index = rn.randint(0, len(message))
            if rn.randint(0, 2) == 1:
                message = message[:index] + alphabet[rn.randint(0, len(alphabet)-1)] + message[index+1:]
            else:
                message = message[:index] + alphabet[rn.randint(0, len(alphabet)-1)] + message[index:]
        if (not rn.randint(0, secondTypo)):
            if (not rn.randint(0, skippedLine)):
                message = ""
            else:                
                index = rn.randint(0, len(message))
                if rn.randint(0, 1):
                    message = message[:index] + alphabet[rn.randint(0, len(alphabet)-1)] + message[index+1:]
                else:
                    message = message[:index] + alphabet[rn.randint(0, len(alphabet)-1)] + message[index:] 
            if (not rn.randint(0, thirdTypo)):
                if (not rn.randint(0, skippedLine)):
                    message = ""
                else:                    
                    index = rn.randint(0, len(message))
                    if rn.randint(0, 1):
                        message = message[:index] + alphabet[rn.randint(0, len(alphabet)-1)] + message[index+1:]
                    else:
                        message = message[:index] + alphabet[rn.randint(0, len(alphabet)-1)] + message[index:]
        
    return message

def allWorkNoPlayParagraphs(message):
    paragraph = ' '*rn.randint(0, 8)
    if rn.randint(0, 10):
        message += '.'
    if rn.randint(0, 3):
        message += ' '
    lines = rn.randint(0, 15) 
    if rn.randint(0, 20):
        for i in range(lines):
            if not rn.randint(0, 3):
                paragraph += allWorkNoPlayLines(message.upper())
            else:
                paragraph += allWorkNoPlayLines(message)
    else:
        for i in range(lines):
            if not rn.randint(0, 3):
                paragraph += "\t\t" + allWorkNoPlayLines(message.upper()) + "\n"
            else:
                paragraph += "\t\t" + allWorkNoPlayLines(message) + "\n"
    return paragraph

jack()
		 */
	}

}
