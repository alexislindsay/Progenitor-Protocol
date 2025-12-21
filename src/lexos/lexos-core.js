/**
 * LexOS Core Implementation
 * Universal Information Architecture
 * Part of the Progenitor Protocol
 *
 * "LexOS is not universal by conversion. LexOS is universal by being."
 */

class LexOS {
    constructor() {
        this.version = "1.0.0-alpha";
        this.quantumField = new Map();
        this.entanglements = new Map();
    }

    /**
     * Create a LexOS seed from content
     * Compresses content to 1KB metadata seed
     *
     * @param {any} content - The content to convert to seed
     * @param {object} options - Optional settings
     * @returns {object} The LexOS seed
     */
    createSeed(content, options = {}) {
        const seed = {
            lexos_version: this.version,
            timestamp: Date.now(),
            seed: {
                hash: this._generateHash(content),
                compressed: this._compress(content),
                coherence: 1.0
            },
            metadata: {
                original_format: options.format || this._detectFormat(content),
                structure: this._analyzeStructure(content),
                entanglements: options.entanglements || []
            }
        };

        // Store in quantum field
        this.quantumField.set(seed.seed.hash, content);

        return seed;
    }

    /**
     * Manifest seed as specific format
     * Collapses quantum superposition into observed format
     *
     * @param {object} seed - The LexOS seed
     * @param {string} format - Desired format (json, html, markdown, text)
     * @returns {string} Manifested content
     */
    manifest(seed, format) {
        const content = this._decompress(seed.seed.compressed);
        
        switch(format.toLowerCase()) {
            case 'json':
                return this._manifestAsJSON(content);
            case 'html':
                return this._manifestAsHTML(content);
            case 'markdown':
            case 'md':
                return this._manifestAsMarkdown(content);
            case 'text':
            case 'txt':
                return this._manifestAsText(content);
            default:
                throw new Error(`Unknown format: ${format}`);
        }
    }

    /**
     * Verify seed coherence
     * Checks if seed maintains quantum coherence
     *
     * @param {object} seed - The LexOS seed to verify
     * @returns {boolean} True if coherent
     */
    verifyCoherence(seed) {
        if (!seed || !seed.seed) return false;
        
        // Check hash integrity
        const content = this._decompress(seed.seed.compressed);
        const expectedHash = this._generateHash(content);
        
        if (seed.seed.hash !== expectedHash) {
            seed.seed.coherence = 0;
            return false;
        }

        // Check metadata
        if (!seed.metadata || !seed.metadata.structure) {
            seed.seed.coherence *= 0.5;
        }

        return seed.seed.coherence > 0.7;
    }

    /**
     * Get entanglements for a seed
     *
     * @param {object} seed - The LexOS seed
     * @returns {array} List of entangled seeds
     */
    getEntanglements(seed) {
        if (!seed.metadata || !seed.metadata.entanglements) {
            return [];
        }
        return seed.metadata.entanglements;
    }

    /**
     * Create entanglement between two seeds
     *
     * @param {object} seed1 - First seed
     * @param {object} seed2 - Second seed
     * @param {string} relationship - Type of relationship
     */
    entangle(seed1, seed2, relationship = 'related') {
        if (!seed1.metadata.entanglements) {
            seed1.metadata.entanglements = [];
        }
        if (!seed2.metadata.entanglements) {
            seed2.metadata.entanglements = [];
        }

        seed1.metadata.entanglements.push({
            hash: seed2.seed.hash,
            relationship: relationship,
            timestamp: Date.now()
        });

        seed2.metadata.entanglements.push({
            hash: seed1.seed.hash,
            relationship: relationship,
            timestamp: Date.now()
        });
    }

    // PRIVATE METHODS

    _generateHash(content) {
        const str = JSON.stringify(content);
        let hash = 0;
        for (let i = 0; i < str.length; i++) {
            const char = str.charCodeAt(i);
            hash = ((hash << 5) - hash) + char;
            hash = hash & hash;
        }
        return hash.toString(36);
    }

    _compress(content) {
        // Simple base64 compression (placeholder for real compression)
        const jsonStr = JSON.stringify(content);
        return btoa(jsonStr);
    }

    _decompress(compressed) {
        const jsonStr = atob(compressed);
        return JSON.parse(jsonStr);
    }

    _detectFormat(content) {
        if (typeof content === 'string') return 'text';
        if (Array.isArray(content)) return 'json-array';
        if (typeof content === 'object') return 'json-object';
        return 'unknown';
    }

    _analyzeStructure(content) {
        if (typeof content !== 'object') {
            return { type: 'primitive', depth: 0 };
        }

        const analyze = (obj, depth = 0) => {
            if (depth > 10) return depth;
            
            let maxDepth = depth;
            for (let key in obj) {
                if (typeof obj[key] === 'object' && obj[key] !== null) {
                    maxDepth = Math.max(maxDepth, analyze(obj[key], depth + 1));
                }
            }
            return maxDepth;
        };

        return {
            type: Array.isArray(content) ? 'array' : 'object',
            depth: analyze(content),
            keys: Object.keys(content)
        };
    }

    _manifestAsJSON(content) {
        return JSON.stringify(content, null, 2);
    }

    _manifestAsHTML(content) {
        const renderValue = (val, level = 0) => {
            const indent = '  '.repeat(level);
            
            if (val === null) return `<span class="null">null</span>`;
            if (typeof val === 'string') return `<span class="string">"${val}"</span>`;
            if (typeof val === 'number') return `<span class="number">${val}</span>`;
            if (typeof val === 'boolean') return `<span class="boolean">${val}</span>`;
            
            if (Array.isArray(val)) {
                return `<ul class="array">
${val.map(item => `${indent}  <li>${renderValue(item, level + 1)}</li>`).join('\n')}
${indent}</ul>`;
            }
            
            if (typeof val === 'object') {
                return `<dl class="object">
${Object.entries(val).map(([k, v]) => 
    `${indent}  <dt>${k}</dt>\n${indent}  <dd>${renderValue(v, level + 1)}</dd>`
).join('\n')}
${indent}</dl>`;
            }
            
            return String(val);
        };

        return `<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>LexOS Manifest</title>
    <style>
        body { font-family: monospace; padding: 20px; }
        .null { color: #808080; }
        .string { color: #008000; }
        .number { color: #0000ff; }
        .boolean { color: #ff0000; }
        .array { list-style: none; padding-left: 20px; }
        .object { padding-left: 20px; }
        dt { font-weight: bold; color: #000080; }
        dd { margin-left: 20px; margin-bottom: 10px; }
    </style>
</head>
<body>
    <h1>LexOS Manifestation</h1>
    <div class="content">
${renderValue(content)}
    </div>
</body>
</html>`;
    }

    _manifestAsMarkdown(content) {
        const renderValue = (val, level = 0) => {
            const indent = '  '.repeat(level);
            
            if (val === null) return 'null';
            if (typeof val === 'string') return `"${val}"`;
            if (typeof val === 'number' || typeof val === 'boolean') return String(val);
            
            if (Array.isArray(val)) {
                return val.map(item => `${indent}- ${renderValue(item, level)}`).join('\n');
            }
            
            if (typeof val === 'object') {
                return Object.entries(val)
                    .map(([k, v]) => `${indent}**${k}**: ${renderValue(v, level + 1)}`)
                    .join('\n\n');
            }
            
            return String(val);
        };

        return `# LexOS Manifestation

${renderValue(content)}

---
*Manifested from quantum information field*`;
    }

    _manifestAsText(content) {
        const renderValue = (val, level = 0) => {
            const indent = '  '.repeat(level);
            
            if (val === null) return 'null';
            if (typeof val !== 'object') return String(val);
            
            if (Array.isArray(val)) {
                return val.map((item, idx) => 
                    `${indent}[${idx}] ${renderValue(item, level + 1)}`
                ).join('\n');
            }
            
            return Object.entries(val)
                .map(([k, v]) => `${indent}${k}: ${renderValue(v, level + 1)}`)
                .join('\n');
        };

        return `LexOS Manifestation\n${'='.repeat(50)}\n\n${renderValue(content)}`;
    }
}

// Export for use
if (typeof module !== 'undefined' && module.exports) {
    module.exports = LexOS;
}
