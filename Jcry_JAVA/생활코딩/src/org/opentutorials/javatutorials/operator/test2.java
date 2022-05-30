package org.opentutorials.javatutorials.operator;

import java.util.Scanner;

public class test2 {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		String A = in.next();
		
		for (int i = A.length()-1; i>=0; i--) {
			System.out.print(A.charAt(i));
		}
		
	}

}
