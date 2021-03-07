import java.util.*;
public class LargestPalindromicSubStr {

	public static boolean isPalindrome(String  str){
		char [] ch =new char[str.length()];
		for (int i = 0; i < ch.length; i++) {
			ch[i]=str.charAt(i);
		}
		int start =0;
		int end = ch.length-1;
		while(start<end){
		if(str.charAt(start)!=str.charAt(end)){
			return false;
		}
		start++;
		end--;
		}
		return true;
		}

	public static void main(String[] args) {
		String Palindrome ="";
	//	Scanner sc = new Scanner(System.in);
	//	String str = sc.nextLine();
		String str="a";
		int n=str.length();
		for (int i = 0; i < n-1; i++) {
			for (int j = i+1; j < n; j++) {
				if((isPalindrome(str.substring(i, j)))&& str.substring(i, j).length()> Palindrome.length()) {
					Palindrome = str.substring(i, j);
					
				}
			}
		}
		System.out.println(Palindrome);

	}

}
