package ecosystem

// Contrato para propuestas de mejora continua
#ImprovementProposal: {
    id: string
    timestamp: string
    source_workflow: string
    category: "performance" | "security" | "reliability" | "documentation" | "architecture"
    description: string
    suggested_action: string

    // Análisis de potencial (Brainstorming)
    analysis?: {
        impact: "high" | "medium" | "low"
        effort: "high" | "medium" | "low"
        risk:   "high" | "medium" | "low"
        novelty_score: >=0 & <=10 | *5
    }

    context_links: [...{

        type: "log" | "manifest" | "source"
        path: string
    }]
    priority?: "low" | "medium" | "high"
    status: "pending" | "analyzed" | "discarded" | "implemented" | *"pending"
    ... // Apertura para datos de diagnóstico extra
}
