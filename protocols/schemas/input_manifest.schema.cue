package ecosystem

// Esquema universal para archivos de entrada de herramientas (Input Manifests)
#InputManifest: {
    // Identificación de la operación
    action: string
    timestamp: string
    
    // Parámetros específicos de la tarea
    params: {
        target_id: string
        path?: string
        metadata?: { [string]: _ }
        [string]: _ // Apertura controlada para parámetros ad-hoc
    }
    
    // Metadata de trazabilidad
    origin: {
        agent: string
        workflow_id: string
    }
}
