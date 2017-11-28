package com.facebook.services;

import javax.ws.rs.Path;
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
@Path("/Port")
public class Port_stat 
{
	@Path("/load_port_stats")
	@POST
	@Produces(MediaType.APPLICATION_JSON)
	public String load_queue_stats(@FormParam("node_id") String node_id,@FormParam("port_id") String port_id,@FormParam("transmit_error") String transmit_error,@FormParam("crc_error") String crc_error,@FormParam("receive_error") String receive_error ,@FormParam("receive_drops") String receive_drops ,@FormParam("transmit_drop") String transmit_drop) 
			            		   throws ClassNotFoundException,SQLException {
		
		try{
			
			 java.sql.Connection con=ConnectionProvider.getCon();
			 
			
			//Check if the user had already liked the post if yes then delete the row(unlike) and if no add one row			    	
			    	
				    String query = "insert into port_stat values(?,?,?,?,?,?,?,now())";
				    java.sql.PreparedStatement stcomment=con.prepareStatement(query);
				 
					 stcomment.setString(1,node_id); 
					 stcomment.setString(2, port_id);
					 stcomment.setString(3,crc_error); 
					 stcomment.setString(4, receive_error);
					 stcomment.setString(5,transmit_error); 
					 stcomment.setString(6, receive_drops);
					 stcomment.setString(7,transmit_drop); 
					
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
