package enigma_assignment;


public class Plugboard extends Translator {

	public Plugboard(String[] pairs) {
		super();
		int l=10;
		// TODO Auto-generated constructor stub
		if (pairs.length<=10)
			l=pairs.length;
		if(l!=0){	
		   for (int i=0 ;i<l ;i++)
		  {
			int index=(int)(I_letter.get(pairs[i].charAt(0)));
			int value=(int)(I_letter.get(pairs[i].charAt(1)));
			ForwardPermutation[index]= value;
			ForwardPermutation[value]= index;
		  }
		}
		for (int i=0 ;i<26 ;i++)
		{
			if (ForwardPermutation[i]==-1)
			{
				ForwardPermutation[i]=i;
				ReversePermutation[i]=i;
			}
		}
		revrese(ForwardPermutation);// fill the reverse permutation
	}
	

}
