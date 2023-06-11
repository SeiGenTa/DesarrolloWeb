package com.auxiliar.confesiones;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.Errors;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;

import jakarta.validation.Valid;


@Controller
@Validated
public class ConfesionController {
  
  @GetMapping("/confesion")
  public String confesionForm(Model model) {
    model.addAttribute("confesion", new Confesion());
    return "confesionForm";
  }

  @PostMapping(value="/confesion")
  public String confesionSubmit(@Valid Confesion confesion, Model model, Errors errors) {
    if (errors.hasErrors()) {
      model.addAttribute("errors", errors);
      return "error";
    }
    model.addAttribute("confesion", confesion);
    return "confesionResult";
  }
  
}
