import java.util.Scanner;
import java.lang.*;

class Extra_Terrestrial{

    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
        String word = input.next();
        StringBuffer word_handling = new StringBuffer(word); 
        System.out.println(word_handling.reverse());

        input.close();
        
    }
}