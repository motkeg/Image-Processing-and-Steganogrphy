package enigma_assignment;


public class Enigma extends Substitutor{

     private Rotor R;
     private Rotor M;
     private Rotor L;
     private Reflector B=new Reflector();
     private Plugboard pb;
     
   ////////////////////////////////////////////////////////  
   public Enigma(int[] rottors, int[] setting,int[] offsets,String[] PBpeirs  )
   {
	 R=new Rotor(rottors[2],setting[2],offsets[2]);
     M=new Rotor(rottors[1],setting[1],offsets[1]);
	 L=new Rotor(rottors[0],setting[0],offsets[0]);
	 pb=new Plugboard(PBpeirs);
   }
   
   @Override
	public char LetterTranslation(char i, char perm) {
		// TODO Auto-generated method stub
		return 0;
	}
	
	//////////encode string
	public String Encode(String s)
	{
		String str=new String();
		int r=s.length();
		for (int i = 0; i < s.length(); i++) {
			if (s.charAt(i)!=' ')
			 str+=LetterTranslation(s.charAt(i));
			else str+=s.charAt(i);
		}
		//System.out.println(str);
		return str;
	}
	
	////////////////////////translation//////////
	public char LetterTranslation(char i) {
		if (R.Notch || M.Notch) {
		  if (M.Notch) 
		      L.Offset(-1); 
		   M.Offset(-1);  
		 }
		 R.Offset(-1);
		 
		 char l=pb.LetterTranslation(i, 'f');
		 l=RML(l); 
		 l=B.LetterTranslation(l, 'f');
		 l=LMR(l);
		 l=pb.LetterTranslation(l, 'r');
		
		 return l;
		
	}
	public char RML(char i){
		 char l=R.LetterTranslation(i,'f');
		 l=M.LetterTranslation(l, 'f');
		 l=L.LetterTranslation(l, 'f');
		 
		 return l;
	}
	public char LMR(char i)
	{
		char l=L.LetterTranslation(i,'r');
		 l=M.LetterTranslation(l, 'r');
		 l=R.LetterTranslation(l, 'r');
		 
		 return l;
	}
	///print the offsets of each rotor
	public String Poffsets()
	{
		String str=new String();
		str=(L.Get('o')+1)+","+(M.Get('o')+1)+","+(R.Get('o')+1);
		//System.out.println(str);
		return str;		
	}
	public  int[] Str2Ind(String Str) {
		int[] indx=new int[Str.length()];
		for (int i = 0; i < Str.length(); i++) {
			indx[i]=B.I_letter.get(Str.charAt(i))+1;
		}
		return indx;
	}
	
	////////////////----------------Main------------------------//////////////////////////////////
	public static void main(String[] args) {

	

		int[] rottors=new int[]{2,5,4};
	    int[] setting=new int[]{19,9,24};
		String[] PBpeirs=new String[]{"ZU", "HL", "CQ", "WM","OA","PY" ,"EB", "TR", "DN", "VI"};//{"AT" ,"CE" ,"RL"};
		
		Enigma E1=new Enigma(rottors, setting, new int[]{3,15,14}, PBpeirs);
		String offStr=E1.Encode("MLD");
		
		int[] offsets=E1.Str2Ind(offStr);//the offset to decode the message
		Enigma E=new Enigma(rottors, setting, offsets, PBpeirs);
		
		System.out.println(E.Poffsets());
		
		System.out.println(E.Encode( "UMDPQCUAQNLVVSPIARKC"
				+ "TTRJQKCFPTOKRGO"
				+ "ZXALDRLPUHAUZSO"
				+ "SZFSUGWFNFDZCUG"
				+ "VEXUULQYXOTCYRP"
				+ "SYGGZHQMAGPZDKC"
				+ "KGOJMMYYDDH"));
		System.out.println(E.Poffsets());
	}
	
	

}
