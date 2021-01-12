import java.util.Scanner;

public class BusRoute {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		for (int i = 0; i < t; i++) {
			int n = sc.nextInt();
			int k = sc.nextInt();
			int arr[] = new int[n];
			for (int j = 0; j < arr.length; j++) {
				arr[j]=sc.nextInt();
			}
			for(int l=arr.length-1;l>=0;l--){
				k-=k%arr[l];
			}
			System.out.println(k);
		}
		
		
		

	}

}
