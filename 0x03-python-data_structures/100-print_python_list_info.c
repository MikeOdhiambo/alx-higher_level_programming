#include <Python.h>

/**
 * print_python_list_info - prints information about a python list
 * @p: Python object
 * Return: void
 */

void print_python_list_info(PyObject *p)
{
	int i;
	PyListObject *obj = (PyListObject *)p;
	long int len = PyList_Size(p);

	printf("[*] Size of the Python List = %li\n", len);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (i = 0; i < len; i++)
	{
		printf("Element %i: %s\n", i, Py_TYPE(obj->ob_item[i])->tp_name);
	}
}
