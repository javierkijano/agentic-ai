package ecosystem

#Skill: #Metadata & {
    kind: "skill"
    status: "active" | "deprecated" | "dev"
    tags?: [...string]
    platforms?: [...string]
    
    interfaces: {
        cli?: {
            enabled: bool
            commands: { [string]: string }
        }
        api?: {
            enabled: bool
            endpoints: { [string]: string }
        }
    }
    
    input_schema?: string
    output_schema?: string
    
    dependencies?: {
        resources?: [...string]
        system?: [...{ id: string, version?: string }]
        packages?: [...{ id: string, version?: string }]
        skills?: [...{
            id: string
            type: "hard" | "soft" | *"hard"
            reason?: string
        }]
    }
    
    storage?: {
        standard_layout: bool
        description?: string
        contract?: string
    }
}
