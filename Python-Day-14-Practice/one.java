
Class Main{
    public static void main(String[] args){
        String str = "hello";
        for(int i=0; i<str.length(); i++){
            char ch = str.charAt(i);
            if(ch.indexOf('aeiou')){
                   System.out.println(ch); 
            }
        }
    }
}