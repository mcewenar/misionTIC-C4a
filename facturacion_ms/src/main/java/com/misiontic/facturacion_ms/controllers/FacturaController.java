package com.misiontic.facturacion_ms.controllers;
import com.misiontic.facturacion_ms.models.Factura;
import  com.misiontic.facturacion_ms.repositories.FacturaRepository;
import org.springframework.web.bind.annotation.*;
import java.util.Date;
import java.util.List;

@RestController
public class FacturaController {
    private final FacturaRepository facturaRepository;
    public FacturaController(FacturaRepository facturaRepository){
        this.facturaRepository = facturaRepository;
    }
    @PostMapping("/factura")
    Factura nerFactura(@RequestBody Factura factura){
        factura.setDate(new Date());
        return facturaRepository.save(factura);
    }
    @GetMapping("/factura/{username}")
    List<Factura> userFactura(@PathVariable String username){
       // Factura userFactura = facturaRepository.findById(username).orElse(null);
        List<Factura> facturas = facturaRepository.findByUsername(username);
        return facturas;

    }
}
