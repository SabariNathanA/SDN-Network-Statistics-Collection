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
 * Servlet implementation class Load_queue_stats
 */
@WebServlet("/Load_queue_stats")
public class Load_queue_stats extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public Load_queue_stats() {
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
		String queue_id = request.getParameter("queue_id");
		String port_id = request.getParameter("port_id");
		String transmit_error = request.getParameter("transmit_error");
		String queuing_delay = request.getParameter("queuing_delay");
			
		String url = AppConstants.BASE_URL+AppConstants.AUTH_URL_QUEUE+"load_queue_stats";
		HttpClient client = new DefaultHttpClient();
		HttpPost post = new HttpPost(url);
  
		List<NameValuePair> postParams = new ArrayList<NameValuePair>();

		NameValuePair queueid = new BasicNameValuePair("queue_id",queue_id);
		NameValuePair portid = new BasicNameValuePair("port_id",port_id);
		NameValuePair transmiterror = new BasicNameValuePair("transmit_error",transmit_error);
		NameValuePair queuingdelay = new BasicNameValuePair("queuing_delay",queuing_delay);
		
		
		
		
		// Add the parameters to the list.
		postParams.add(queueid);
		postParams.add(portid);
		postParams.add(transmiterror);
		postParams.add(queuingdelay);

		
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
