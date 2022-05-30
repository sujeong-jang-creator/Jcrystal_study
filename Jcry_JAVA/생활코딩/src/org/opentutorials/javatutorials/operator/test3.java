package org.opentutorials.javatutorials.operator;

public class test3 {
	public static void main(String[] args) {
		String string="ABCDEF";
		String A="";
		
		for (int i=string.length()-1;i>=0;i--){
			A = A + string.charAt(i);
		}
		
		System.out.println(A);
	}
}
