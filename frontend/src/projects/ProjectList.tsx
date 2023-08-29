import { useState } from 'react';
import { Project } from './Project';
import ProjectCard from './ProjectCard';
import ProjectForm from './ProjectForm';

interface ProjectListProps {
    projects: Project[];
    onSave: (project: Project) => void;
}

function ProjectList({ projects, onSave }: ProjectListProps) {
    const [ projectToEdit, setProjectToEdit ] = useState({});

    const handleEdit = (project: Project) => {
        setProjectToEdit(project);
    }
    const cancelEditing = () => {
        setProjectToEdit({});
    }

    return (
    <div className='row'>
        {projects.map((project) => (
            <div key={project.id} className='cols-sm'>
                {project === projectToEdit ? (
                    <ProjectForm onCancel={cancelEditing} onSave={onSave} project={project}/>
                ) : (
                    <ProjectCard project={project} onEdit={handleEdit} />
                )}
            </div>
        ))}
    </div>
)}

export default ProjectList;