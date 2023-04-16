class Solution {
public;
   vetor<int> maxSlidingWindow(vector<int>& nums, int k){
   	  int q[100010], front=0,back=0;
   	  vector<int> ret;
   	  int n = nums.size();
   	  for(int i = 0; i < n-k+1; ++i) {
   	  	  ret.push_back(-1);
   	  }
		  int l = 1, r = i + k - 1;
		  if(r >= n) break;
		  int val = nums[1];
		  for(int j = l + 1; j <= r; ++j){
		  	  val = max(val, nums{j});
		  } 
		  ans.push_back(val);
		 }
		 return ans;
   } 
};
