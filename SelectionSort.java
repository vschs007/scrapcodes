public class SelectionSort {

	public static void main(String[] args) {
		int[] arr ={2,6,12,9,0,3,6,56};
		int n=arr.length;
		for(int i=0;i<n-1;i++){
			int imin=i;
			for(int j=i+1;j<n;j++){
				if(arr[j]<arr[imin]){
					imin=j;
				int temp=arr[i];
				arr[i]=arr[imin];
				arr[imin]=temp;
			}
			
			
		}

		}
		for(int k=0;k<n;k++){
			System.out.println(arr[k]);
		}
	}
	}
		

	


