public class ReverseInteger {
    public int reverse(int x) {
    
        long xy = (long)x;
        String str = Long.toString(xy);
        int length = str.length();
        if (xy < 0) {
            length--;
        }
            
        System.out.println(length);
    
        double utemp = Math.pow(10,(length-1));
        double ltemp = 10;
    
        int count = 1;
            
        int val = (int) (xy / utemp);
        int value = (int) (xy % ltemp);
        xy = (long) (xy - (val*utemp));
        xy = (long) (xy + (value*utemp));
        xy = (long) (xy - (value*(ltemp/10)));
        xy = (long) (xy + (val*(ltemp/10)));	
    
        
        utemp /= 10;
        ltemp *= 10;
    
        while (count < (length/2)) {
            val = (int) (x / utemp) % 10;
            value = (int) ((int) (xy % ltemp) / Math.pow(10, count));
            xy = (long) (xy - (val*utemp));
            xy = (long) (xy + (value*utemp));
            xy = (long) (xy - (value*(ltemp/10)));
            xy = (long) (xy + (val*(ltemp/10)));
        
            utemp /= 10;
            ltemp *= 10;
                    
            count++;
        }
            
        if (xy > Math.pow(2,31) - 1 || xy < Math.pow(-2,31)){
            return 0;
        }
        x = (int)xy;
        return x;
    }
}

