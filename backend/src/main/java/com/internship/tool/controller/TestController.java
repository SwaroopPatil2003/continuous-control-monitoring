package com.internship.tool.controller;

import com.internship.tool.service.AiServiceClient;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/test")
public class TestController {

    private final AiServiceClient aiServiceClient;

    public TestController(AiServiceClient aiServiceClient) {
        this.aiServiceClient = aiServiceClient;
    }

    @GetMapping("/secure")
    public String testSecure() {
        return aiServiceClient.validateInput("Explain control monitoring");
    }

    @GetMapping("/report")
    public String testReport() {
        return aiServiceClient.generateReport("Generate report");
    }
}