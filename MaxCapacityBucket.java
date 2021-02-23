
public class MaxCapacityBucket {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int arr[] ={1,2,3,4,5,6};
		int n =arr.length;
		int l=0;
		int r = n-1;
		int area=0;
		while(l<r){
			area=Math.max(area,(Math.min(arr[l], arr[r])*(r-l)));
			if(arr[l]<arr[r]){
				l+=1;
			}
			else{
				r-=1;
			}
		}
		System.out.println(area);
	}

}
