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

@Path("/Routing")
public class Routing_info {


	@SuppressWarnings("null")
	@Path("/get_routing_info")
	@POST
	@Produces(MediaType.APPLICATION_JSON)
	public String getlikes(@FormParam("src_ip") String src_ip,@FormParam("dest_ip") String dest_ip
			               ) 
			            		   throws ClassNotFoundException,SQLException {
		
		try{
			
			 java.sql.Connection con=ConnectionProvider.getCon();
			 
			
				    	
				    String query = "select intermediate_switch_ip, port_id from routing_info where src_ip=? and dest_ip=? ";
				    java.sql.PreparedStatement stcomment=con.prepareStatement(query);
				 
					 stcomment.setString(1,src_ip); 
					 stcomment.setString(2, dest_ip);
					
					 ResultSet rs= stcomment.executeQuery();
					 
					 JSONObject datas=null;
						JSONArray array = new JSONArray();
						while(rs!=null && rs.next())
						{
							datas= new JSONObject();
							
							datas.put("intermediate_switch_ip",rs.getString("intermediate_switch_ip"));
							datas.put("port_id",rs.getString("port_id"));
							array.put(datas);
							
								
						}
						JSONObject result = new JSONObject();
						result.put("Data", array);   

					       String json= result.toString();
				         return json;
                      }
	catch (Exception e) 
		{
			e.printStackTrace();
			
		}

		return "trying...";
			
	}


}

