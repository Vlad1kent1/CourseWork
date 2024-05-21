package com.example.Coursework_back.controllers;

import com.example.Coursework_back.models.Application;
import com.example.Coursework_back.repositories.ApplicationRepository;
import jakarta.validation.Valid;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/applications")
public class ApplicationController {

    @Autowired
    private ApplicationRepository applicationRepository;

    @GetMapping
    public ResponseEntity<List<Application>> getAllApplication(){
        return ResponseEntity.ok(applicationRepository.findAll());
    }

    @GetMapping("/{id}")
    public ResponseEntity<Optional<Application>> getApplication(@PathVariable Long id){
        return ResponseEntity.ok(applicationRepository.findById(id));
    }

    @PostMapping
    public ResponseEntity<Application> createApplication(@Valid @RequestBody Application application){
        applicationRepository.save(application);
        return ResponseEntity.ok().build();
    }

    @PutMapping("/{id}")
    public ResponseEntity<Application> updateApplication(@PathVariable Long id, @RequestBody Application application){
        application.setId(id);
        applicationRepository.save(application);
        return ResponseEntity.ok().build();
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Application> deleteApplication(@PathVariable Long id){
        Application application = applicationRepository.findById(id).get();
        applicationRepository.delete(application);
        return ResponseEntity.ok().build();
    }
}
