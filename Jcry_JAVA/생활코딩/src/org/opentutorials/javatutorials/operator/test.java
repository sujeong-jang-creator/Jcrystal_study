package org.opentutorials.javatutorials.operator;

public class test {
	public static void main(String[] args) {
		String string="ABCDEF";
				
		StringBuffer sb = new StringBuffer(string);
		String reverse=sb.reverse().toString();
		
		System.out.println(reverse);
	}
}
