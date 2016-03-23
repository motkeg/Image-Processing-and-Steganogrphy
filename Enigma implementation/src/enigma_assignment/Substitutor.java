package enigma_assignment;
import java.awt.List;
import java.util.Arrays;
import java.util.Hashtable;
import java.util.Objects;


public abstract class Substitutor {
	//index to letter
	 static char[] S_letter= new char[]{'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'};
	 //letter to index
    static Hashtable<Character,Integer> I_letter=new Hashtable<Character,Integer>(); 
    
     
     //permutations from 5 rotors
     String[] perms=new String[]{"EKMFLGDQVZNTOWYHXUSPAIBRCJ",
    		                     "AJDKSIRUXBLHWTMCQGZNPYFVOE",
    		                     "BDFHJLCPRTXVZNYEIWGAKMUSQO",
    		                     "ESOVPZJAYQUIRHXLNFTGKDCMWB",
    		                     "VZBRGITYUPSDNHLXAWMJQOFECK"};
     //notches
     String[] notchs=new String[]{"QR","EF","VW","JK","ZA"};
     
    public Substitutor(){
    	if(I_letter.isEmpty())
    		Fill();}
	public abstract char LetterTranslation(char i, char perm);
	public  void Fill()//default method to fill the dictionary
	{
		for (int i=0 ;i<26 ;i++)
		{
			I_letter.put( S_letter[i], i);
		}
	}
	
	
}
