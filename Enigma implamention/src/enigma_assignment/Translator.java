package enigma_assignment;


public class Translator extends Substitutor {

	int[] ForwardPermutation=new int[26];//forward
    int[] ReversePermutation =new int[26] ;//reverse
	
	
	public Translator()
	{
		//Fill();
	 for (int i=0 ;i<26 ;i++){
		ForwardPermutation[i]=-1;
		ReversePermutation[i]=-1;
		}
	}
	/////////create reverse permutation
	public void revrese(int[] permotation) {
		for (int i=0 ;i<26 ;i++)
		{
			ReversePermutation[permotation[i]]=i;		
		}
	}
	///print reverse or forward permutations
   public void printPer(char a)
   { 
	   String str=new String();
	   if(a=='f' || a=='F'){
	   for (int i=0 ;i<26 ;i++)
		   str+=S_letter[ForwardPermutation[i]];
		   
     }
      if(a=='r' || a=='R'){
    	  for (int i=0 ;i<26 ;i++)
    		  str+=S_letter[ReversePermutation[i]];
   		   
        }
      System.out.println(str);
    }
   ///////////////////letter translation
	public char LetterTranslation(char i, char perm) {
		if(perm=='f' || perm=='f')
		return S_letter[ForwardPermutation[I_letter.get(i)]];
		if(perm=='R' || perm=='r')
			return S_letter[ReversePermutation[I_letter.get(i)]];
		else return 0;
		
	}
	public static void main(String[] args) {
		Reflector b= new Reflector();
		System.out.println(b.I_letter.get('M'));
	}
	
}
