// You're given two  string check if one is the permutation of the other
//
// #Check if they have the same length. If not, fail fast.

public boolean checkPermutation (String stringA, String stringB ){

      String stringA = "cat";
      String stringB = "tac";
      boolean arePermutations = false;

      if (stringA.length() != stringB.length()){
          return arePermutations;
      }

      HashMap<String, Integer> hmap = new HashMap<String, Integer>();
      for(int i = 0; i < stringA.length(); i++){
        hmap.put(stringA.charAt(i), );
      }

      for(int i = 0; i < stringB.length(); i++){
        letters[stringB.charAt(i)]--;
        if(letters[stringB.charAt(i)] < 0){
          retunr arePermutations;
        }
      }
      arePermutations = true;
      return arePermutations;
}
