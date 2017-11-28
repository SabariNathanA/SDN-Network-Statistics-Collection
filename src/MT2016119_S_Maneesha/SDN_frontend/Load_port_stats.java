package com.facebook.servlets;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.apache.http.HttpResponse;
import org.apache.http.NameValuePair;
import org.apache.http.client.HttpClient;
import org.apache.http.client.entity.UrlEncodedFormEntity;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.message.BasicNameValuePair;

import com.facebook.constants.AppConstants;

/**
 * Servlet implementation class Load_port_stats
 */
@WebServlet("/Load_port_stats")
public class Load_port_stats extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public Load_port_stats() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		response.getWriter().append("Served at: ").append(request.getContextPath());
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		String node_id = request.getParameter("node_id");
		String port_id = request.getParameter("port_id");
		String crc_error = request.getParameter("crc_error");
		String receive_error = request.getParameter("receive_error");
		String transmit_error = request.getParameter("transmit_error");
		String receive_drops = request.getParameter("receive_drops");
		String transmit_drop = request.getParameter("transmit_drop");
		
		String url = AppConstants.BASE_URL+AppConstants.AUTH_URL_PORT+"load_port_stats";
		HttpClient client = new DefaultHttpClient();
		HttpPost post = new HttpPost(url);
  
		List<NameValuePair> postParams = new ArrayList<NameValuePair>();

		NameValuePair nodeid = new BasicNameValuePair("node_id",node_id);
		NameValuePair portid = new BasicNameValuePair("port_id",port_id);
		NameValuePair crcerror = new BasicNameValuePair("crc_error",crc_error);
		NameValuePair receiveerror = new BasicNameValuePair("receive_error",receive_error);
		NameValuePair transmiterror = new BasicNameValuePair("transmit_error",transmit_error);
		NameValuePair receivedrops = new BasicNameValuePair("receive_drops",receive_drops);
		NameValuePair transmitdrop = new BasicNameValuePair("transmit_drop",transmit_drop);
		
		
		
		// Add the parameters to the list.
		postParams.add(nodeid);
		postParams.add(portid);
		postParams.add(crcerror);
		postParams.add(receiveerror);
		postParams.add(transmiterror);
		postParams.add(receivedrops);
		postParams.add(transmitdrop);
		
		post.setEntity(new UrlEncodedFormEntity(postParams));
		HttpResponse rsp = client.execute(post);
		BufferedReader rd = new BufferedReader(new InputStreamReader(rsp
				.getEntity().getContent()));
         
		String line = "";
		String output="";
		while ((line = rd.readLine()) != null) {
			//System.out.println(line);
			output += line + System.getProperty("line.separator");
		}
		System.out.println(output);
		PrintWriter out = response.getWriter();
      
		
		out.println(output);
		out.close();

	}

}
