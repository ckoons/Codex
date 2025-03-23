# Claude Development Notes - Forge Project

This file contains development notes for working with Claude on the Forge project.

## Project Overview

Forge is an AI-powered design and fabrication tool that helps users create and manufacture physical objects. It uses Claude for design guidance, optimization, and manufacturing process planning.

### Key Components

1. **Design Interface**: Cloud-based CAD/CAM system with AI assistance
2. **Materials Database**: Comprehensive information about materials properties and manufacturing constraints
3. **Optimization Engine**: AI-driven system to optimize designs for performance, cost, and manufacturability
4. **Manufacturing Pipeline**: Automated process planning and CNC/3D printer instructions
5. **Documentation Generator**: Automated technical documentation and assembly instructions

## Development Guidelines

### Code Style

- Use TypeScript for frontend components
- Python for backend services and AI integration
- Follow PEP 8 for Python code
- Consistent 2-space indentation for TypeScript/JavaScript

### Architecture

- Microservices architecture with containerized components
- FastAPI for Python backend services
- React with Material UI for frontend
- PostgreSQL for structured data, MongoDB for unstructured data
- Redis for caching and message queuing

### AI Integration

- Claude API for design assistance, optimization, and documentation
- Vision models for design recognition and analysis
- Embeddings for similarity search in design database
- LLM for natural language interaction with CAD tools

## Implementation Roadmap

### Phase 1: MVP (Current)

- Basic CAD interface with Claude design assistance
- Simple materials selection
- Basic optimization for a limited set of parameters
- Support for standard manufacturing processes (3D printing, basic CNC)

### Phase 2: Enhanced Optimization

- Multi-parameter optimization (strength, weight, cost, time)
- Advanced material selection and comparison tools
- Topology optimization with physics simulation
- Support for additional manufacturing techniques

### Phase 3: Advanced Features

- Assembly planning and simulation
- Full manufacturing pipeline integration
- Collaborative design tools with real-time assistance
- Design marketplace and sharing capabilities

## Commit Message Format

```
feat: Add concise description of feature

- Detailed bullet points about implementation
- Technical considerations or challenges addressed
- References to relevant issues or documentation

🤖 Generated with [Claude Code](https://claude.ai/code)
Co-Authored-By: Casey Koons <cskoons@gmail.com> & Claude <noreply@anthropic.com>
```

## Testing Strategy

- Unit tests for all core functions
- Integration tests for API endpoints
- End-to-end tests for critical user journeys
- Performance testing for optimization algorithms
- Load testing for concurrent user scenarios

## Useful Commands

```bash
# Start development environment
docker-compose up -d

# Run backend tests
cd backend && pytest

# Run frontend tests
cd frontend && npm test

# Build production containers
docker-compose -f docker-compose.prod.yml build

# Deploy to staging
./scripts/deploy.sh staging

# Monitor logs
docker-compose logs -f
```

## Latest Updates (March 2025)

1. Completed integration with Claude API for design assistance
2. Added initial optimization engine for simple mechanical parts
3. Implemented materials database with basic properties
4. Created prototype UI for CAD interaction with Claude
5. Added support for STL and STEP file formats
6. Implemented basic document generation for manufacturing

## Next Steps

1. Enhance the optimization engine with multi-parameter capabilities
2. Improve Claude's understanding of mechanical design principles
3. Add support for assembly design and constraints
4. Implement collaborative features for team-based design
5. Integrate with additional manufacturing services and platforms

## Meeting Notes

### March 15, 2025

- Discussed optimization algorithm performance improvements
- Planned integration with additional CAD file formats
- Reviewed UI design for material selection interface
- Identified bottlenecks in the rendering pipeline
- Agreed on priorities for next sprint