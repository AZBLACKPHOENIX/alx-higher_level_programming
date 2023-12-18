#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Print Python list info
 * @p: PyObject pointer
 */
void print_python_list(PyObject *p)
{
    Py_ssize_t size, i;
    PyObject *item;

    printf("[*] Python list info\n");
    size = PyList_Size(p);
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; ++i)
    {
        item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}

/**
 * print_python_bytes - Print Python bytes info
 * @p: PyObject pointer
 */
void print_python_bytes(PyObject *p)
{
    Py_ssize_t size, i;
    char *str;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    str = PyBytes_AsString(p);

    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", str);

    printf("  first 10 bytes: ");
    for (i = 0; i < size && i < 10; ++i)
    {
        printf("%02x ", (unsigned char)str[i]);
    }
    printf("\n");
}

/**
 * print_python_float - Print Python float info
 * @p: PyObject pointer
 */
void print_python_float(PyObject *p)
{
    printf("[.] float object info\n");

    if (!PyFloat_Check(p))
    {
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }

    printf("  value: %f\n", ((PyFloatObject *)p)->ob_fval);
}

