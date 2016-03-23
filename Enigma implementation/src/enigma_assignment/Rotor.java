package enigma_assignment;


public class Rotor extends Translator {
	  private int offset=0;
	  private int Setting=0;
	  private char[] notch=new char[2];
	  boolean  Notch=false;

	////////////////////////////////////////////////////////////  
	public Rotor(int ind ,int set ,int off)
	{
		 for (int i=0 ;i<26 ;i++)
		  {
			  ForwardPermutation[i]=I_letter.get(perms[ind-1].charAt(i));
		  }
		  revrese(ForwardPermutation);
		  
		  notch[0]=notchs[ind-1].charAt(0);
		  notch[1]=notchs[ind-1].charAt(1);
		  this.Offset(off-1);
		  Setting=set-1;
	}
	
	@Override
	public char LetterTranslation(char i, char perm) {
		
	  int ind=(I_letter.get(i)+offset-Setting+26)%26;
	  int permletter=I_letter.get(super.LetterTranslation(S_letter[ind], perm));
	  char l=S_letter [(permletter-offset+ Setting +26)%26];
	  return l;
	}
	//////advance or put value to offset
	public void Offset(int f)
	{
		if(f==-1){
			
			if (++offset==I_letter.get(notch[0]))
			{  
			 Notch=true;
			}
			else { Notch=false;}
			if(offset ==26)offset=0;
		}
		else {
			   offset=f;
			   if (offset==I_letter.get(notch[0])) Notch=true;
			}
	}
	////////get offset or setting
	public int Get(char a)
	{
		if(a=='o') return offset;
		if(a=='s') return Setting;
		else
			return 0;
	}
	
	

}
