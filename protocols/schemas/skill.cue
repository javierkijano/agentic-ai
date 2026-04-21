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
    
    storage?: {
        standard_layout: bool
        description?: string
        contract?: string
    }
}
