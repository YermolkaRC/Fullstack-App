import { useEffect, useState } from "react";
import { MOCK_PROJECTS } from "./MockProjects";
import { Project } from "./Project";
import ProjectList from "./ProjectList";
import { projectAPI } from "./projectAPI";
import useInfiniteScroll from "../hooks/UseInfiniteScroll";

function ProjectsPage() {
    const [projects, setProjects] = useState<Project[]>([]);
    const [loading, setLoading] = useInfiniteScroll(loadMoreProjects);
    const [error, setError] = useState<string | undefined>(undefined);
    const [currentPage, setCurrentPage] = useState(1);
    const [loadedAll, setLoadedAll] = useState(false);

    useEffect(() => {
        setLoading(true);
    }, [])

    function loadMoreProjects () {
        if (loadedAll) {
            setLoading(false);
            return;
        }
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
                setCurrentPage((prevPage) => prevPage + 1);
            })
            .catch((e) => {
                setLoading(false);
                if (e instanceof Error) {
                    setError(e.message);
                }
            })
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