package enigma_assignment;


public class Reflector extends Translator {
	
  public Reflector()
  {
	  super();
	  String perm="YRUHQSLDPXNGOKMIEBFZCWVJAT";// permutation for reflector

	  for (int i=0 ;i<26 ;i++)
	  {
		  ForwardPermutation[i]=I_letter.get(perm.charAt(i));
	  }
	  revrese(ForwardPermutation);
  }
}
