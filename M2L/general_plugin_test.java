package eu.securedfp7.m2lservice.plugin;


import java.io.File;

import javax.xml.bind.JAXBException;

public class general_plugin_test {
	
	
	public static void main(String[] args) {
		
		
		String MSPLFileName = "anonymity_mspl.xml";
		String securityControlFileName = "test.conf";
				
		
		long startTime = System.currentTimeMillis();
		M2LPlugin genericPlugin = new M2LPlugin();
		genericPlugin.getConfiguration(MSPLFileName, securityControlFileName);
		long stopTime = System.currentTimeMillis();
		long elapsedTime = stopTime - startTime;
	    System.out.println(elapsedTime);
	}
}
