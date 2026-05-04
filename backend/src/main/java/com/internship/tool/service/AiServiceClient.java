package com.internship.tool.service;

import org.springframework.http.*;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;
import org.springframework.web.client.ResourceAccessException;
import org.springframework.http.client.SimpleClientHttpRequestFactory;
import java.util.HashMap;
import java.util.Map;

@Service
public class AiServiceClient {

    private final RestTemplate restTemplate;

    private final String AI_BASE_URL = "http://localhost:5000";

    

    public AiServiceClient() {
        SimpleClientHttpRequestFactory factory = new SimpleClientHttpRequestFactory();
        factory.setConnectTimeout(10000); // 10 seconds
        factory.setReadTimeout(10000);    // 10 seconds

        this.restTemplate = new RestTemplate(factory);
    }

    // 🔹 CALL /secure-input
    public String validateInput(String input) {
        try {
            String url = AI_BASE_URL + "/secure-input";

            Map<String, String> body = new HashMap<>();
            body.put("input", input);

            HttpHeaders headers = new HttpHeaders();
            headers.setContentType(MediaType.APPLICATION_JSON);

            HttpEntity<Map<String, String>> request =
                    new HttpEntity<>(body, headers);

            ResponseEntity<String> response =
                    restTemplate.postForEntity(url, request, String.class);

            return response.getBody();

        } catch (Exception e) {
            System.out.println("Error calling /secure-input: " + e.getMessage());
            return null; // ✅ graceful fallback
        }
    }

    // 🔹 CALL /generate-report
    public String generateReport(String input) {
        try {
            String url = AI_BASE_URL + "/generate-report";

            Map<String, String> body = new HashMap<>();
            body.put("input", input);

            HttpHeaders headers = new HttpHeaders();
            headers.setContentType(MediaType.APPLICATION_JSON);

            HttpEntity<Map<String, String>> request =
                    new HttpEntity<>(body, headers);

            ResponseEntity<String> response =
                    restTemplate.postForEntity(url, request, String.class);

            return response.getBody();

        } catch (Exception e) {
            System.out.println("Error calling /generate-report: " + e.getMessage());
            return null; // ✅ graceful fallback
        }
    }
}