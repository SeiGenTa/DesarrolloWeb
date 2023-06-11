package com.auxiliar.confesiones;

import jakarta.validation.constraints.Min;
import jakarta.validation.constraints.NotNull;
import jakarta.validation.constraints.Size;


public class Confesion {

  @NotNull
  @Min(1)
  private long id;

  @NotNull
  @Size(min = 3)
  private String titulo;
  
  private String cuerpo;
  
  private String[] tags;


  public Confesion() {

  }

  /* Getters y Setters */

  public long getId() {
    return id;
  }

  public void setId(long id) {
    this.id = id;
  }

  public String getTitulo() {
    return titulo;
  }

  public void setTitulo(String titulo) {
    this.titulo = titulo;
  }

  public String getCuerpo() {
    return cuerpo;
  }

  public void setCuerpo(String cuerpo) {
    this.cuerpo = cuerpo;
  }

  public String[] getTags() {
    return tags;
  }

  public void setTags(String[] tags) {
    this.tags = tags;
  }

}
