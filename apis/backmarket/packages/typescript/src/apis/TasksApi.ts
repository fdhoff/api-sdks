// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type { ErrorResponseV1, Task } from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation } from '../runtime/index.js';

const getWsTask: Operation = {
  id: 'get-ws-task',
  method: 'GET',
  path: '/ws/tasks/{taskId}',
  resource: 'tasks',
  name: 'get',
  params: [{ wire: 'taskId', name: 'taskId', location: 'path' }],
};

export const OPERATIONS: readonly Operation[] = [getWsTask];

export class TasksApi extends Resource {
  /** Get the state of a background task. */
  get(taskId: number): Promise<Task> {
    return this.call(getWsTask, undefined, { taskId });
  }
}
