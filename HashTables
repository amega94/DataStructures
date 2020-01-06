//TODO1: Test this Code
//And check out TODO2 below

public class HelloWorld{

     public static void main(String []args){
        System.out.println("Hello World");
     }
}

class HashTable{
    
    int arrSize;
    String [] hashArray;
    
    public HashTable(int arrSize)
    {
        if (isPrime(arrSize)){
            this.arrSize = arrSize;
            hashArray = new String[this.arrSize];
            
        }
        else{
            this.arrSize = nextPrime(arrSize);
            hashArray = new String[this.arrSize];
        }
    }
    
    //Returns ideal index location
    private int HashFunx1 (String str){
        int hashVal = str.hashCode()
        hashVal = hashVal % this.arraySize;
        //The above ensures that hashVal is within bounds
        //of array size
        
        if (hashVal < 0){
            hasVal = hasVal + this.arraySize -1;
            //Should hashVal be negative, % will normalize it to be
            //in the range (-arrSize+1,0) inclusive.
            //hashVal can be negative since .hashCode() returns
            //a value in the range of int.
            //int has range (-2^31,2^31-1) inclusive
            //By adding  arrSize-1, we can
            //make the range (0,arrSz)
        }
        return hashVal
    }
    
    //Returns step size
    private int HashFunx2 (String str){
        int hashVal = str.hashCode()
        hashVal = hashVal % this.arraySize;
        if (hashVal < 0){
            hasVal = hasVal + (this.arraySize -1);
        }
        
        //The below is done through research. The 3 is a prime number and must be less than the array size.
        
        //2 is also a good option since its unlikely that the array
        //Size is smaller than 2. 2 is also the smallest prime #
        return 3 - hashVal % 3;
    }
    
    // This f(x) inserts data into the hashing table
    public void insert (String str)
    {
        int hashVal = HashFunx1(str)
        int step = HashFunx2(str) //this method is called once
        
        while (hashArray[index] != null)
        {
            hashVal = hashVal + step;
            hashVal = hashVal % this.arraySize;
        }
        
        hashArray[hashVal] = word; //finally inserting
        return;
    }
    
    public String find (String str){
        int hashVal = HashFunx1(str)
        int step = HashFunx2(str) //this method is called once
        
        
        //TODO2: The logic as per the video is NOT correct
        while (hashArray[hashVal] != null)
        {
            if(hashArray[hashVal].equals(str)){
                return hashArray[hashVal];
            }
            hashVal = hashVal + step;
            hashVal = hashVal % this.arraySize;
        }
        
        return hashArray[hashVal];
        //The video is WRONG. This will NOT hit this line
        //If the hashArray[hashVal] is NULL.
    }
    
    
    private boolean isPrime (int n)
    {
        if ( n <= 1 ) return false;
        else {
            for (int i = 2; i*i <= n; i++){
             if ( n % i == 0) return false;
            }
        }
        return true
    }
    private int nextPrime (int n){
        for (int i = n+1; true; i++ )
        {
            if (isPrime(i)) return true;
        }
    }
    
    
}
