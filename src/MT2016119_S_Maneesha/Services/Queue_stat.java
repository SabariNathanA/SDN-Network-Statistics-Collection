package com.facebook.services;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

import javax.ws.rs.FormParam;
import javax.ws.rs.POST;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;

import org.json.JSONArray;
import org.json.JSONObject;

import com.facebook.services.beans.Like;
import com.facebook.services.beans.User;
import com.google.gson.Gson;

import dBConn.ConnectionProvider;

@Path("/Queue")
public class Queue_stat {


	@SuppressWarnings("null")
	@Path("/getqueue_instant_stats")
	@POST
	@Produces(MediaType.APPLICATION_JSON)
	public String getqueue_instant_stats(@FormParam("queue_id") String queue_id,@FormParam("port_id") String port_id
			               ) 
			            		   throws ClassNotFoundException,SQLException {
		
		try{
			
			 java.sql.Connection con=ConnectionProvider.getCon();
			 
			
			//Check if the user had already liked the post if yes then delete the row(unlike) and if no add one row			    	
			    	
				    String query = "select queue_id, port_id,transmit_error,queuing_delay from queue_stat where queue_id=? and port_id=? and insert_time=(select max(insert_time) from queue_stat where queue_id=? and port_id=? )";
				    java.sql.PreparedStatement stcomment=con.prepareStatement(query);
				 
					 stcomment.setString(1,queue_id); 
					 stcomment.setString(2, port_id);
					 stcomment.setString(3,queue_id); 
					 stcomment.setString(4, port_id);
					 ResultSet rs= stcomment.executeQuery();
					 while(rs.next())
						{
							
							 System.out.println(rs.getString(3));
							 System.out.println(rs.getLong(4));
						}
				    
				     return new Gson().toJson("commentinserted");
                      }
	catch (Exception e) 
		{
			e.printStackTrace();
			
		}

		return "trying...";
			
	}
	@Path("/load_queue_stats")
	@POST
	@Produces(MediaType.APPLICATION_JSON)
	public String load_queue_stats(@FormParam("queue_id") String queue_id,@FormParam("port_id") String port_id,@FormParam("transmit_error") String transmit_error,@FormParam("queuing_delay") String queuing_delay               ) 
			            		   throws ClassNotFoundException,SQLException {
		
		try{
			
			 java.sql.Connection con=ConnectionProvider.getCon();
			 
			
			//Check if the user had already liked the post if yes then delete the row(unlike) and if no add one row			    	
			    	
				    String query = "insert into queue_stat values(?,?,?,?,now())";
				    java.sql.PreparedStatement stcomment=con.prepareStatement(query);
				 
					 stcomment.setString(1,queue_id); 
					 stcomment.setString(2, port_id);
					 stcomment.setString(3,transmit_error); 
					 stcomment.setString(4, queuing_delay);
				 stcomment.executeUpdate();
					return new Gson().toJson("insertsuccessful");
                      }
	catch (Exception e) 
		{
			e.printStackTrace();
			
		}

		return "trying...";
			
	}


}

