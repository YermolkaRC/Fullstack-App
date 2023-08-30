import { useEffect, useState } from "react";
import { MOCK_PROJECTS } from "./MockProjects";
import { Project } from "./Project";
import ProjectList from "./ProjectList";
import { projectAPI } from "./projectAPI";

function ProjectsPage() {
    const [projects, setProjects] = useState<Project[]>([]);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState<string | undefined>(undefined);
    const [currentPage, setCurrentPage] = useState(1);
    const [loadedAll, setLoadedAll] = useState(false);

    useEffect(() => {
        setLoading(true);
        projectAPI.get(currentPage)
            .then((data) => {
                setError(undefined);
                setLoading(false);
                if (data.length === 0) {
                    setLoadedAll(true);
                    return;
                }
                if (currentPage === 1) {
                    setProjects(data);
                } else {
                    setProjects((projects) => [...projects, ...data]);
                }
            })
            .catch((e) => {
                setLoading(false);
                if (e instanceof Error) {
                    setError(e.message);
                }
            })
    }, [currentPage])
    useEffect(() => {
        window.addEventListener('scroll', handleScroll);
        return () => window.removeEventListener('scroll', handleScroll);
    }, [])
    function handleScroll() {
        if (window.innerHeight + document.documentElement.scrollTop !== document.documentElement.scrollHeight) return;
        if (loading || error || loadedAll) return;
        setCurrentPage((prevPage) => prevPage + 1);
        console.log('Fetching')
    }
    const saveProject = (project: Project) => {
        projectAPI.put(project)
            .then((updatedProject) => {
                let updatedProjects = projects.map((p: Project) => {
                    return p.id === project.id ? new Project(updatedProject) : p;
                })
                setProjects(updatedProjects);
            })
            .catch((e) => {
                if (e instanceof Error) {
                    setError(e.message);
                }
            })
    }

    return (
    <>
        <h1>Projects</h1>
        {error && (
            <div className="row">
                <div className="card large error">
                    <section>
                        <p>
                            <span className="icon-alert inverse"></span>
                            {error}
                        </p>
                    </section>
                </div>
            </div>
        )}
        <ProjectList projects={projects} onSave={saveProject} />
        {loading && (
            <div className="center-page">
                <span className="spinner primary"></span>
                <p>Loading...</p>
            </div>
        )}
    </>
  );
}

export default ProjectsPage